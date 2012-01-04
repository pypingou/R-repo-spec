%global packname  simboot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Simultaneous Confidence Intervals and Adjusted p--values for Diversity Indices

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-boot R-mvtnorm 

%description
Package simboot provides estimation of simultaneous bootstrap and
asymptotic confidence intervals for diversity indices, namely the Shannon
and the Simpson index. Possible pre-specified multiple comparison types
are Dunnett and Tukey. Further user-defined contrast matrices are
applicable. In addition, simboot estimates adjusted as well as unadjusted
p--values for two of the three proposed bootstrap methods.

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
%doc %{rlibdir}/simboot/NEWS
%doc %{rlibdir}/simboot/html
%doc %{rlibdir}/simboot/DESCRIPTION
%{rlibdir}/simboot/INDEX
%{rlibdir}/simboot/help
%{rlibdir}/simboot/data
%{rlibdir}/simboot/Meta
%{rlibdir}/simboot/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora