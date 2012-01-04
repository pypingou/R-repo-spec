%global packname  TSPC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Prediction using time-course gene expression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-superpc R-survival 

BuildRequires:    R-devel tex(latex) R-superpc R-survival 

%description
Performs survival and quantitative outcome using time-course gene
expression, described in the following paper:Zhang Y, Tibshirani RJ, Davis
RW. Predicting patient survival from longitudinal gene expression. Stat
Appl Genet Mol Biol. 2010;9(1):Article41. Epub 2010 Nov 22.

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
%doc %{rlibdir}/TSPC/html
%doc %{rlibdir}/TSPC/DESCRIPTION
%{rlibdir}/TSPC/Meta
%{rlibdir}/TSPC/INDEX
%{rlibdir}/TSPC/R
%{rlibdir}/TSPC/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora