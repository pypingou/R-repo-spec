%global packname  Rtreemix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          Rtreemix: Mutagenetic trees mixture models.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graph R-Biobase 
Requires:         R-methods R-graph R-Biobase R-Hmisc 

BuildRequires:    R-devel tex(latex) R-methods R-graph R-Biobase
BuildRequires:    R-methods R-graph R-Biobase R-Hmisc 


%description
Rtreemix is a package that offers an environment for estimating the
mutagenetic trees mixture models from cross-sectional data and using them
for various predictions. It includes functions for fitting the trees
mixture models, likelihood computations, model comparisons, waiting time
estimations, stability analysis, etc.

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
%doc %{rlibdir}/Rtreemix/doc
%doc %{rlibdir}/Rtreemix/DESCRIPTION
%doc %{rlibdir}/Rtreemix/html
%{rlibdir}/Rtreemix/data
%{rlibdir}/Rtreemix/INDEX
%{rlibdir}/Rtreemix/R
%{rlibdir}/Rtreemix/help
%{rlibdir}/Rtreemix/NAMESPACE
%{rlibdir}/Rtreemix/libs
%{rlibdir}/Rtreemix/examples
%{rlibdir}/Rtreemix/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora