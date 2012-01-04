%global packname  Rwinsteps
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Running Winsteps in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Rwinsteps package facilitates communication between R and the Rasch
modeling software Winsteps. The package currently includes functions for
reading and writing command files, sending them to Winsteps, reading and
writing data according to command file specifications, reading output into
R, and plotting various results.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/Rwinsteps/html
%doc %{rlibdir}/Rwinsteps/NEWS
%doc %{rlibdir}/Rwinsteps/DESCRIPTION
%{rlibdir}/Rwinsteps/R
%{rlibdir}/Rwinsteps/help
%{rlibdir}/Rwinsteps/NAMESPACE
%{rlibdir}/Rwinsteps/INDEX
%{rlibdir}/Rwinsteps/Meta
%{rlibdir}/Rwinsteps/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora