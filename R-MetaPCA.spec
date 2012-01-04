%global packname  MetaPCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          MetaPCA: Meta-analysis in the Dimension Reduction of Genomic data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-foreach 

BuildRequires:    R-devel tex(latex) R-foreach 

%description
MetaPCA implements simultaneous dimension reduction using PCA when
multiple studies are combined. We propose two basic ideas to find a common
PC subspace by eigenvalue maximization approach and angle minimization
approach, and we extend the concept to incorporate Robust PCA and Sparse
PCA in the meta-analysis realm.

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
%doc %{rlibdir}/MetaPCA/html
%doc %{rlibdir}/MetaPCA/DESCRIPTION
%{rlibdir}/MetaPCA/help
%{rlibdir}/MetaPCA/NAMESPACE
%{rlibdir}/MetaPCA/INDEX
%{rlibdir}/MetaPCA/Meta
%{rlibdir}/MetaPCA/R
%{rlibdir}/MetaPCA/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora