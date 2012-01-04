%global packname  MADAM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          This package provides some basic methods for meta-analysis

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-qvalue R-RankProd R-RColorBrewer R-GeneMeta R-gplots R-genefilter R-impute 

BuildRequires:    R-devel tex(latex) R-Biobase R-qvalue R-RankProd R-RColorBrewer R-GeneMeta R-gplots R-genefilter R-impute 

%description
In this package we provide some basic utilities for performing
meta-analysis. We included methods for dealing with missing values, or
measurements with a variance of zero. For developing or testing
meta-analysis methods a mock up data model is integrated. Additionally did
we implement a method for performing significance based methods proposed
by Fisher and Rhodes. For visualizing the results three methods were
added. Some functions were taken from the GeneMeta and RankProd packages
in order to implement parallel versions of the existing methods. Please
refer to the original authors if you make use of these implementations.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora