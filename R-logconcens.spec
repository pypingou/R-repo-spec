%global packname  logconcens
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11.2
Release:          1%{?dist}
Summary:          Maximum likelihood estimation of a log-concave density based on censored data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-base R-methods R-utils R-grDevices R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-base R-methods R-utils R-grDevices R-graphics R-stats 

%description
Based on right or interval censored data, compute the maximum likelihood
estimator of a density under the assumption that it is log-concave. For
further information see Duembgen, Schuhmacher, and Rufibach (2011,

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
%doc %{rlibdir}/logconcens/DESCRIPTION
%doc %{rlibdir}/logconcens/html
%{rlibdir}/logconcens/INDEX
%{rlibdir}/logconcens/NAMESPACE
%{rlibdir}/logconcens/help
RPM build errors:
%{rlibdir}/logconcens/R
%{rlibdir}/logconcens/libs
%{rlibdir}/logconcens/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11.2-1
- initial package for Fedora