%global packname  tripack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          Triangulation of irregularly spaced data

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A constrained two-dimensional Delaunay triangulation package

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
%doc %{rlibdir}/tripack/html
%doc %{rlibdir}/tripack/DESCRIPTION
%{rlibdir}/tripack/NAMESPACE
%{rlibdir}/tripack/LICENSE
%{rlibdir}/tripack/Meta
%{rlibdir}/tripack/libs
%{rlibdir}/tripack/help
%{rlibdir}/tripack/R
%{rlibdir}/tripack/data
%{rlibdir}/tripack/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.4-1
- initial package for Fedora