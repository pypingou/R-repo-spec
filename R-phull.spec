%global packname  phull
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          p-hull: a generalization of convex hull, X-Y hull and bounding rectangle

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package computes the p-hull of a finite planar set, which is a
generalization of the convex hull, X-Y hull and bounding rectangle. A
fast, O(n log n) Graham-scan based routine is used.

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
%doc %{rlibdir}/phull/html
%doc %{rlibdir}/phull/DESCRIPTION
%doc %{rlibdir}/phull/doc
%{rlibdir}/phull/R
%{rlibdir}/phull/Meta
%{rlibdir}/phull/help
%{rlibdir}/phull/demo
%{rlibdir}/phull/NAMESPACE
%{rlibdir}/phull/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora