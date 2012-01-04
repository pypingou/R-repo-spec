%global packname  raster
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.41
Release:          1%{?dist}
Summary:          Geographic analysis and modeling with raster data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-41.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp 

BuildRequires:    R-devel tex(latex) R-methods R-sp 

%description
Reading, writing, manipulating, analyzing and modeling of gridded spatial
data. The package implements basic and high-level functions, as well as
map algebra. Processing of very large files is supported.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.41-1
- initial package for Fedora