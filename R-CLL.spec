%global packname  CLL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.11
Release:          1%{?dist}
Summary:          A Package for CLL Gene Expression Data

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-affy R-Biobase 


BuildRequires:    R-devel tex(latex) R-affy R-Biobase



%description
The CLL package contains the chronic lymphocytic leukemia (CLL) gene
expression data.  The CLL data had 24 samples that were either classified
as progressive or stable in regards to disease progression.  The data came
from Dr. Sabina Chiaretti at Division of Hematology, Department of
Cellular Biotechnologies and Hematology, University La Sapienza, Rome,
Italy and Dr. Jerome Ritz at Department of Medicine, Brigham and Women's
Hospital, Harvard Medical School, Boston, Massachusetts.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.11-1
- initial package for Fedora