%global packname  prim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.12
Release:          1%{?dist}
Summary:          Patient Rule Induction Method (PRIM)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
PRIM for bump hunting in high-dimensional data

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
%doc %{rlibdir}/prim/html
%doc %{rlibdir}/prim/DESCRIPTION
%doc %{rlibdir}/prim/doc
%{rlibdir}/prim/NAMESPACE
%{rlibdir}/prim/Meta
%{rlibdir}/prim/R
%{rlibdir}/prim/help
%{rlibdir}/prim/INDEX
%{rlibdir}/prim/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.12-1
- initial package for Fedora