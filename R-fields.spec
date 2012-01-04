%global packname  fields
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          6.6.2
Release:          1%{?dist}
Summary:          Tools for spatial data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-spam 

BuildRequires:    R-devel tex(latex) R-methods R-spam 

%description
Fields is for curve, surface and function fitting with an emphasis on
splines, spatial data and spatial statistics. The major methods include
cubic, robust, and thin plate splines, and Kriging for large data sets.
The splines and Kriging methods are supporting by functions that can
determine the smoothing parameter (nugget and sill variance) by cross
validation and also by restricted maximum likelihood.  A major feature is
that any covariance function implemented in R with the fields interface
can be used for spatial prediction. Some tailored optimization functions
are supplied for find the MLEs for the Matern family of covariances. There
are also many useful functions for plotting and working with spatial data
as images. This package also contains an implementation of a sparse matrix
methods for large data sets and currently requires the sparse matrix
(spam) package for testing (but not for the standard spatial functions.)
Use help(fields) to get started and for an overview.  The fields source
code is heavily commented and should provide useful explanation of
numerical details in addition to the manual pages.

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
%doc %{rlibdir}/fields/html
%doc %{rlibdir}/fields/DESCRIPTION
%{rlibdir}/fields/help
%{rlibdir}/fields/R
%{rlibdir}/fields/INDEX
%{rlibdir}/fields/LICENSE
%{rlibdir}/fields/NAMESPACE
%{rlibdir}/fields/libs
%{rlibdir}/fields/data
RPM build errors:
%{rlibdir}/fields/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 6.6.2-1
- initial package for Fedora