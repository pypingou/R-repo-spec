%global packname  SpatialNP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multivariate nonparametric methods based on spatial signs and ranks

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ICSNP 

BuildRequires:    R-devel tex(latex) R-ICSNP 

%description
This package contains test and estimates of location, tests of
independence, tests of sphericity and several estimates of shape all based
on spatial signs, symmetrized signs, ranks and signed ranks.

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
%doc %{rlibdir}/SpatialNP/html
%doc %{rlibdir}/SpatialNP/DESCRIPTION
%{rlibdir}/SpatialNP/help
%{rlibdir}/SpatialNP/INDEX
%{rlibdir}/SpatialNP/Meta
%{rlibdir}/SpatialNP/NAMESPACE
%{rlibdir}/SpatialNP/R

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora