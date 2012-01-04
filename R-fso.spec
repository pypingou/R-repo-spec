%global packname  fso
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Fuzzy Set Ordination

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Fuzzy set ordination is a multivariate analysis used in ecology to relate
the composition of samples to possible explanatory variables.  While
differing in theory and method, in practice, the use is similar to
"constrained ordination." The package contains plotting and summary
functions as well as the analyses

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
%doc %{rlibdir}/fso/html
%doc %{rlibdir}/fso/DESCRIPTION
%{rlibdir}/fso/help
%{rlibdir}/fso/R
%{rlibdir}/fso/INDEX
%{rlibdir}/fso/Meta
%{rlibdir}/fso/NAMESPACE
%{rlibdir}/fso/ChangeLog

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora