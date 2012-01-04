%global packname  FunCluster
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.09
Release:          1%{?dist}
Summary:          Functional Profiling of Microarray Expression Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-cluster 

BuildRequires:    R-devel tex(latex) R-Hmisc R-cluster 

%description
FunCluster performs a functional analysis of microarray expression data
based on Gene Ontology & KEGG functional annotations. From expression data
and functional annotations FunCluster builds classes of putatively
co-regulated biological processes through a specially designed clustering

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
%doc %{rlibdir}/FunCluster/DESCRIPTION
%doc %{rlibdir}/FunCluster/html
%{rlibdir}/FunCluster/INDEX
%{rlibdir}/FunCluster/Meta
%{rlibdir}/FunCluster/data
%{rlibdir}/FunCluster/help
%{rlibdir}/FunCluster/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.09-1
- initial package for Fedora