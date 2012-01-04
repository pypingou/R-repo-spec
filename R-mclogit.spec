%global packname  mclogit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Mixed Conditional Logit

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-MASS R-memisc R-Matrix 

BuildRequires:    R-devel tex(latex) R-stats R-MASS R-memisc R-Matrix 

%description
This packages provides a function to estimate parameters for the mixed
conditional logit model, or conditional logit with random effects. The
current implementation is limited to random intercepts and to the PQL
technique, mainly appropriate for large clusters.

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
%doc %{rlibdir}/mclogit/html
%doc %{rlibdir}/mclogit/DESCRIPTION
%{rlibdir}/mclogit/data
%{rlibdir}/mclogit/Meta
%{rlibdir}/mclogit/demo
%{rlibdir}/mclogit/R
%{rlibdir}/mclogit/NAMESPACE
%{rlibdir}/mclogit/INDEX
%{rlibdir}/mclogit/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora