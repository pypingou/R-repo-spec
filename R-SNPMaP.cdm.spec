%global packname  SNPMaP.cdm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Annotation for SNP Microarrays and Pooling in R

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Pooling DNA on SNP microarrays is a cost-effective way to carry out
genome-wide association studies for heritable disorders or traits. The
SNPMaP package provides formal SNPMaP objects and methods in R as a base
for these analyses using Affymetrix genotyping arrays. The SNPMaP.cdm
package provides cdm objects for the SNPMaP package.

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
%doc %{rlibdir}/SNPMaP.cdm/DESCRIPTION
%doc %{rlibdir}/SNPMaP.cdm/html
%doc %{rlibdir}/SNPMaP.cdm/CITATION
%{rlibdir}/SNPMaP.cdm/Meta
%{rlibdir}/SNPMaP.cdm/INDEX
%{rlibdir}/SNPMaP.cdm/NAMESPACE
%{rlibdir}/SNPMaP.cdm/data
%{rlibdir}/SNPMaP.cdm/help

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora