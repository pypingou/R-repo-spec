%global packname  MetaQC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          MetaQC: Objective Quality Control and Inclusion/Exclusion Criteria for Genomic Meta-Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-proto R-foreach 


BuildRequires:    R-devel tex(latex) R-proto R-foreach



%description
MetaQC implements our proposed quantitative quality control measures: (1)
internal homogeneity of co-expression structure among studies (internal
quality control; IQC); (2) external consistency of co-expression structure
correlating with pathway database (external quality control; EQC); (3)
accuracy of differentially expressed gene detection (accuracy quality
control; AQCg) or pathway identification (AQCp); (4) consistency of
differential expression ranking in genes (consistency quality control;
CQCg) or pathways (CQCp). (See the reference for detailed explanation.)
For each quality control index, the p-values from statistical hypothesis
testing are minus log transformed and PCA biplots were applied to assist
visualization and decision. Results generate systematic suggestions to
exclude problematic studies in microarray meta-analysis and potentially
can be extended to GWAS or other types of genomic meta-analysis. The
identified problematic studies can be scrutinized to identify technical
and biological causes (e.g. sample size, platform, tissue collection,
preprocessing etc) of their bad quality or irreproducibility for final
inclustion/exclusion decision.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora