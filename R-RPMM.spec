%global packname  RPMM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.06
Release:          1%{?dist}
Summary:          Recursively Partitioned Mixture Model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster 

BuildRequires:    R-devel tex(latex) R-cluster 

%description
Recursively Partitioned Mixture Model for Beta and Gaussian Mixtures. This
is a model-based clustering algorithm that returns a hierarchy of classes,
similar to hierarchical clustering, but also similar to finite mixture

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
%doc %{rlibdir}/RPMM/DESCRIPTION
%doc %{rlibdir}/RPMM/html
%{rlibdir}/RPMM/help
%{rlibdir}/RPMM/data
%{rlibdir}/RPMM/NAMESPACE
%{rlibdir}/RPMM/Meta
%{rlibdir}/RPMM/INDEX
%{rlibdir}/RPMM/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.06-1
- initial package for Fedora