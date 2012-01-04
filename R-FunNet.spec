%global packname  FunNet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.00.12
Release:          1%{?dist}
Summary:          Integrative Functional Analysis of Transcriptional Networks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.00-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ade4 R-cluster R-Hmisc R-nlme R-sna R-Cairo 


BuildRequires:    R-devel tex(latex) R-ade4 R-cluster R-Hmisc R-nlme R-sna R-Cairo



%description
FunNet is an integrative tool for analyzing gene co-expression networks
built from microarray expression data. The analytic model implemented in
this library involves two abstraction layers: transcriptional and
functional (biological roles). A functional profiling technique using Gene
Ontology & KEGG annotations is applied to extract a list of relevant
biological themes from microarray expression profiling data. Afterwards
multiple-instance representations are built to relate significant themes
to their transcriptional instances (i.e. the two layers of the model). An
adapted non-linear dynamical system model is used to quantify the
proximity of relevant genomic themes based on the similarity of the
expression profiles of their gene instances. Eventually an unsupervised
multiple-instance clustering procedure, relying on the two abstraction
layers, is used to identify the structure of the co-expression network
composed from modules of functionally related transcripts. Functional and
transcriptional maps of the co-expression network are provided separately
together with detailed information on the network centrality of related
transcripts and genomic themes.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.00.12-1
- initial package for Fedora