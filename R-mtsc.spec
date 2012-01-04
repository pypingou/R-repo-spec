%global packname  mtsc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Multivariate Timeseries Clusters

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-s3x 

BuildRequires:    R-devel tex(latex) R-s3x 

%description
A package for multivariate timeseries clustering. Currently, this includes
constrained agglomerative clustering over observations (and extensions for
change point detection), based closely on the work of Harnish, Nelson and
Runger (2009). This package is incomplete and experimental.

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
%doc %{rlibdir}/mtsc/html
%doc %{rlibdir}/mtsc/DESCRIPTION
%{rlibdir}/mtsc/INDEX
%{rlibdir}/mtsc/Meta
%{rlibdir}/mtsc/R
%{rlibdir}/mtsc/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora