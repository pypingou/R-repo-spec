%global packname  validator
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          External and Internal Validation Indices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-clv R-clValid R-flexclust R-mlbench 

BuildRequires:    R-devel tex(latex) R-clv R-clValid R-flexclust R-mlbench 

%description
This package contains external and internal validation indices. The
internal validation functions are mainly implemented in "cclust" and
revised with small changes. The external validation functions are using
the similarity table from the package "clv" and further external indices
are included in this package.

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
%doc %{rlibdir}/validator/html
%doc %{rlibdir}/validator/DESCRIPTION
%{rlibdir}/validator/help
%{rlibdir}/validator/Meta
%{rlibdir}/validator/INDEX
%{rlibdir}/validator/R

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora