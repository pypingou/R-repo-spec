%global packname  diffGeneAnalysis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.36.0
Release:          1%{?dist}
Summary:          Performs differential gene expression Analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-graphics R-grDevices R-minpack.lm R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-minpack.lm R-stats R-utils 


%description
Analyze microarray data

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
%doc %{rlibdir}/diffGeneAnalysis/html
%doc %{rlibdir}/diffGeneAnalysis/DESCRIPTION
%doc %{rlibdir}/diffGeneAnalysis/doc
%{rlibdir}/diffGeneAnalysis/INDEX
%{rlibdir}/diffGeneAnalysis/R
%{rlibdir}/diffGeneAnalysis/help
%{rlibdir}/diffGeneAnalysis/data
%{rlibdir}/diffGeneAnalysis/Meta
%{rlibdir}/diffGeneAnalysis/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.36.0-1
- initial package for Fedora