%global packname  penalizedSVM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Feature Selection SVM using penalty functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-e1071 R-MASS R-corpcor R-statmod R-tgp R-mlegp R-lhs 


BuildRequires:    R-devel tex(latex) R-e1071 R-MASS R-corpcor R-statmod R-tgp R-mlegp R-lhs



%description
This package provides feature selection SVM using penalty functions. The
smoothly clipped absolute deviation (SCAD), 'L1-norm', 'Elastic Net'
('L1-norm' and 'L2-norm') and 'Elastic SCAD' (SCAD and 'L2-norm')
penalties are availible. The tuning parameters can be founf using either a
fixed grid or a interval search.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora