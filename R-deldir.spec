%global packname  deldir
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.16
Release:          1%{?dist}
Summary:          Delaunay Triangulation and Dirichlet (Voronoi) Tessellation.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-16.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.

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
%doc %{rlibdir}/deldir/DESCRIPTION
%doc %{rlibdir}/deldir/html
%{rlibdir}/deldir/err.list
%{rlibdir}/deldir/ratfor
%{rlibdir}/deldir/help
%{rlibdir}/deldir/READ_ME
%{rlibdir}/deldir/INDEX
%{rlibdir}/deldir/NAMESPACE
%{rlibdir}/deldir/R
%{rlibdir}/deldir/Meta
%{rlibdir}/deldir/ex.out
%{rlibdir}/deldir/code.discarded
%{rlibdir}/deldir/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.16-1
- initial package for Fedora