%global packname  timsac
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          TIMe Series Analysis and Control package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Time series analysis and control program package TIMSAC.

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
%doc %{rlibdir}/timsac/doc
%doc %{rlibdir}/timsac/DESCRIPTION
%doc %{rlibdir}/timsac/LICENCE
%doc %{rlibdir}/timsac/html
%{rlibdir}/timsac/NAMESPACE
%{rlibdir}/timsac/INDEX
%{rlibdir}/timsac/help
%{rlibdir}/timsac/Meta
RPM build errors:
%{rlibdir}/timsac/data
%{rlibdir}/timsac/R
%{rlibdir}/timsac/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora