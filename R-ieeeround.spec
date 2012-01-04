%global packname  ieeeround
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Functions to set and get the IEEE rounding mode

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A pair of functions for getting and setting the IEEE rounding mode for
floating point computations.

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
%doc %{rlibdir}/ieeeround/DESCRIPTION
%doc %{rlibdir}/ieeeround/NEWS
%doc %{rlibdir}/ieeeround/html
%{rlibdir}/ieeeround/NAMESPACE
%{rlibdir}/ieeeround/R
%{rlibdir}/ieeeround/INDEX
%{rlibdir}/ieeeround/Meta
%{rlibdir}/ieeeround/libs
%{rlibdir}/ieeeround/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora