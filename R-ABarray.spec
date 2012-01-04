%global packname  ABarray
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Microarray QA and statistical data analysis for Applied Biosystems Genome Survey Microrarray (AB1700) gene expression data.

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-Biobase R-graphics R-grDevices R-methods R-multtest R-stats R-tcltk R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-Biobase R-graphics R-grDevices R-methods R-multtest R-stats R-tcltk R-utils 


%description
Automated pipline to perform gene expression analysis for Applied
Biosystems Genome Survey Microarray (AB1700) data format. Functions
include data preprocessing, filtering, control probe analysis, statistical
analysis in one single function. A GUI interface is also provided. The raw
data, processed data, graphics output and statistical results are
organized into folders according to the analysis settings used.

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
%doc %{rlibdir}/ABarray/doc
%doc %{rlibdir}/ABarray/DESCRIPTION
%doc %{rlibdir}/ABarray/html
%{rlibdir}/ABarray/help
%{rlibdir}/ABarray/R
%{rlibdir}/ABarray/NAMESPACE
%{rlibdir}/ABarray/INDEX
%{rlibdir}/ABarray/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora