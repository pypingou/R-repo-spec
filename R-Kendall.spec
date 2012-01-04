%global packname  Kendall
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Kendall rank correlation and Mann-Kendall trend test

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes the Kendall rank correlation and Mann-Kendall trend test. See
documentation for use of block bootstrap when there is autocorrelation.

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
%doc %{rlibdir}/Kendall/DESCRIPTION
%doc %{rlibdir}/Kendall/html
%doc %{rlibdir}/Kendall/NEWS
%{rlibdir}/Kendall/NAMESPACE
%{rlibdir}/Kendall/Meta
%{rlibdir}/Kendall/R
%{rlibdir}/Kendall/libs
%{rlibdir}/Kendall/data
%{rlibdir}/Kendall/INDEX
%{rlibdir}/Kendall/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora