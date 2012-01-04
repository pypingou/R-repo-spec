%global packname  JM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Joint Modeling of Longitudinal and Survival Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-nlme R-splines R-survival 

BuildRequires:    R-devel tex(latex) R-MASS R-nlme R-splines R-survival 

%description
Shared parameter models for the joint modeling of longitudinal and
time-to-event data.

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
%doc %{rlibdir}/JM/CITATION
%doc %{rlibdir}/JM/DESCRIPTION
%doc %{rlibdir}/JM/html
%doc %{rlibdir}/JM/NEWS
%{rlibdir}/JM/NAMESPACE
%{rlibdir}/JM/INDEX
%{rlibdir}/JM/data
%{rlibdir}/JM/help
%{rlibdir}/JM/Meta
%{rlibdir}/JM/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora