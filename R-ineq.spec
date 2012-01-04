%global packname  ineq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.9
Release:          1%{?dist}
Summary:          Measuring Inequality, Concentration, and Poverty

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics R-grDevices 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-grDevices 

%description
Inequality, concentration, and poverty measures. Lorenz curves (empirical
and theoretical).

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
%doc %{rlibdir}/ineq/html
%doc %{rlibdir}/ineq/DESCRIPTION
%{rlibdir}/ineq/data
%{rlibdir}/ineq/Meta
%{rlibdir}/ineq/R
%{rlibdir}/ineq/help
%{rlibdir}/ineq/INDEX
%{rlibdir}/ineq/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.9-1
- initial package for Fedora