%global packname  equate
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Statistical Methods for Test Score Equating

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The equate package contains functions for non-IRT equating under both
random groups and nonequivalent groups with anchor test designs. Mean,
linear, equipercentile and circle-arc equating are supported, as are
methods for univariate and bivariate presmoothing of score distributions.
Specific equating methods currently supported include synthetic, nominal
weights, Tucker, Levine observed score, Levine true score, Braun/Holland,
frequency estimation, and chained equating.

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
%doc %{rlibdir}/equate/NEWS
%doc %{rlibdir}/equate/html
%doc %{rlibdir}/equate/doc
%doc %{rlibdir}/equate/DESCRIPTION
%{rlibdir}/equate/INDEX
%{rlibdir}/equate/Meta
%{rlibdir}/equate/LICENSE
%{rlibdir}/equate/help
%{rlibdir}/equate/NAMESPACE
%{rlibdir}/equate/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora