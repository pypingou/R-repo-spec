%global packname  rgrs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.16
Release:          1%{?dist}
Summary:          Functions to make R usage in social sciences easier (in french)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-16.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides functions for beginners and social sciences students
or researchers. Currently it includes functions for cross-tabulation,
weighting, results export, and maps plotting. The documentation and help
pages are written in french.

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
%doc %{rlibdir}/rgrs/DESCRIPTION
%doc %{rlibdir}/rgrs/html
%{rlibdir}/rgrs/INDEX
%{rlibdir}/rgrs/help
%{rlibdir}/rgrs/data
%{rlibdir}/rgrs/Meta
%{rlibdir}/rgrs/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.16-1
- initial package for Fedora