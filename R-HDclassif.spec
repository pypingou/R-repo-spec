%global packname  HDclassif
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          High Dimensionnal Supervised Classification and Clustering

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-MASS 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-MASS 

%description
New disciminant analysis and data clustering methods for high dimensional
data, based on the asumption that high-dimensional data live in different
subspaces with low dimensionality proposing a new parametrization of the
Gaussian mixture model which combines the ideas of dimension reduction and
constraints on the model.

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
%doc %{rlibdir}/HDclassif/DESCRIPTION
%doc %{rlibdir}/HDclassif/html
%{rlibdir}/HDclassif/INDEX
%{rlibdir}/HDclassif/demo
%{rlibdir}/HDclassif/NAMESPACE
%{rlibdir}/HDclassif/data
%{rlibdir}/HDclassif/R
%{rlibdir}/HDclassif/Meta
%{rlibdir}/HDclassif/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora