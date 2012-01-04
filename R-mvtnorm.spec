%global packname  mvtnorm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.9991
Release:          1%{?dist}
Summary:          Multivariate Normal and t Distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-9991.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes multivariate normal and t probabilities, quantiles, random
deviates and densities.

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
%doc %{rlibdir}/mvtnorm/NEWS
%doc %{rlibdir}/mvtnorm/html
%doc %{rlibdir}/mvtnorm/doc
%doc %{rlibdir}/mvtnorm/CITATION
%doc %{rlibdir}/mvtnorm/DESCRIPTION
%{rlibdir}/mvtnorm/help
%{rlibdir}/mvtnorm/NAMESPACE
%{rlibdir}/mvtnorm/INDEX
%{rlibdir}/mvtnorm/Meta
%{rlibdir}/mvtnorm/CHANGES
%{rlibdir}/mvtnorm/R
%{rlibdir}/mvtnorm/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.9991-1
- initial package for Fedora