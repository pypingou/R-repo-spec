%global packname  rEMM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Extensible Markov Model (EMM) for Data Stream Clustering in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-proxy R-cluster R-MASS R-clusterGeneration R-igraph 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-proxy R-cluster R-MASS R-clusterGeneration R-igraph 

%description
This package implements TRACDS (Temporal Relationships between Clusters
for Data Streams) which is a generalization of Extensible Markov Model
(EMM). TRACDS adds a temporal or order model to data stream clustering by
superimposing a dynamically adapting Markov Chain. This package implements
EMM (TRACDS on top of tNN data stream clustering). Development of this
package was supported in part by NSF IIS-0948893.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora