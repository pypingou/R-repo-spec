%global packname  spacetime
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.7
Release:          1%{?dist}
Summary:          classes and methods for spatio-temporal data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp R-zoo R-xts 
Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-sp R-zoo R-xts
BuildRequires:    R-lattice 


%description
A package with classes and methods for spatio-temporal data. In
particular, space-time regular lattices, sparse lattices, and irregular
data are supported, with limited support for trajectories, but not for
topologies with S/T interactions such as space-time prisms. Utility
functions are provided for plotting data as map sequences (lattice or
animation) or multiple time series; for spatial and temporal selection, as
well as methods for retrieving coordinates, for subsetting, print,
summary, etc.

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
%doc %{rlibdir}/spacetime/html
%doc %{rlibdir}/spacetime/DESCRIPTION
%doc %{rlibdir}/spacetime/doc
%{rlibdir}/spacetime/demo
%{rlibdir}/spacetime/help
%{rlibdir}/spacetime/NAMESPACE
%{rlibdir}/spacetime/INDEX
%{rlibdir}/spacetime/data
%{rlibdir}/spacetime/R
%{rlibdir}/spacetime/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.7-1
- initial package for Fedora