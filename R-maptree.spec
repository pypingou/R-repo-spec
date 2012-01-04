%global packname  maptree
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.6
Release:          1%{?dist}
Summary:          Mapping, pruning, and graphing tree models

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster R-rpart 

BuildRequires:    R-devel tex(latex) R-cluster R-rpart 

%description
Functions with example data for graphing, pruning, and mapping models from
hierarchical clustering, and classification and regression trees.

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
%doc %{rlibdir}/maptree/DESCRIPTION
%doc %{rlibdir}/maptree/html
%{rlibdir}/maptree/help
%{rlibdir}/maptree/README
%{rlibdir}/maptree/INDEX
%{rlibdir}/maptree/Meta
%{rlibdir}/maptree/R
%{rlibdir}/maptree/data
%{rlibdir}/maptree/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.6-1
- initial package for Fedora