%global packname  PP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Person Parameter estimation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-splines 

%description
The PP package includes estimation of (MLE and WLE) person parameters for
the 3-PL model (three parameter logistic model) and the GPCM (generalized
partial credit model). The parameters are estimated under the assumption
that the other parameters are known and fixed. The PP package also
provides two functions to estimate person parameters for the 1-PL (Rasch
Model). The package could be useful when items from an itempool/itembank
with known item parameters are administered to a new population of
testtakers and an ability estimation for every testtaker is needed.

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
%doc %{rlibdir}/PP/html
%doc %{rlibdir}/PP/DESCRIPTION
%{rlibdir}/PP/R
%{rlibdir}/PP/Meta
%{rlibdir}/PP/help
%{rlibdir}/PP/INDEX
%{rlibdir}/PP/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora