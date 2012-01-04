%global packname  BradleyTerry
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.8
Release:          1%{?dist}
Summary:          Bradley-Terry Models -- this package is now deprecated in favour of 'BradleyTerry2'

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-brglm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-brglm 


%description
Specify and fit the Bradley-Terry model and structured versions

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
%doc %{rlibdir}/BradleyTerry/doc
%doc %{rlibdir}/BradleyTerry/DESCRIPTION
%doc %{rlibdir}/BradleyTerry/html
%{rlibdir}/BradleyTerry/Meta
%{rlibdir}/BradleyTerry/NAMESPACE
%{rlibdir}/BradleyTerry/data
%{rlibdir}/BradleyTerry/INDEX
%{rlibdir}/BradleyTerry/R
%{rlibdir}/BradleyTerry/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.8-1
- initial package for Fedora