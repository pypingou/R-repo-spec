%global packname  stratification
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Univariate Stratification of Survey Populations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package performs univariate stratification of survey populations. The
main function implements a generalization of the Lavallee-Hidiroglou
method of stratum construction. The generalized method takes into account
a discrepancy between the stratification variable and the survey variable.
The determination of the optimal boundaries also incorporate, if desired,
an anticipated non-response, a take-all stratum for large units, and a
take-none stratum for small units. The well known cumulative root
frequency rule of Dalenius and Hodges and the geometric rule of Gunning
and Horgan are also implemented.

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
%doc %{rlibdir}/stratification/NEWS
%doc %{rlibdir}/stratification/html
%doc %{rlibdir}/stratification/DESCRIPTION
%{rlibdir}/stratification/NAMESPACE
%{rlibdir}/stratification/INDEX
%{rlibdir}/stratification/help
%{rlibdir}/stratification/R
%{rlibdir}/stratification/libs
%{rlibdir}/stratification/Meta
%{rlibdir}/stratification/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.3-1
- initial package for Fedora