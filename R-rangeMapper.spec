%global packname  rangeMapper
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.6
Release:          1%{?dist}
Summary:          A platform for the study of macroecology of life history traits

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-RSQLite R-RSQLite.extfuns R-sp R-rgdal R-maptools R-lattice R-RColorBrewer R-tcltk R-tcltk2 R-pixmap R-classInt 


BuildRequires:    R-devel tex(latex) R-methods R-utils R-RSQLite R-RSQLite.extfuns R-sp R-rgdal R-maptools R-lattice R-RColorBrewer R-tcltk R-tcltk2 R-pixmap R-classInt



%description
A package to manipulate species range (extent-of-occurrence) maps, mainly
tools for easy generation of biodiversity (species richness) or
life-history traits maps.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.6-1
- initial package for Fedora