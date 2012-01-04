%global packname  eba
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.7.0
Release:          1%{?dist}
Summary:          Elimination-by-Aspects (EBA) Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Fitting and testing multi-attribute probabilistic choice models,
especially the Bradley-Terry-Luce (BTL) model (Bradley & Terry, 1952;
Luce, 1959), elimination-by-aspects (EBA) models (Tversky, 1972), and
preference tree (Pretree) models (Tversky & Sattath, 1979).

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
%doc %{rlibdir}/eba/DESCRIPTION
%doc %{rlibdir}/eba/CITATION
%doc %{rlibdir}/eba/html
%{rlibdir}/eba/data
%{rlibdir}/eba/NAMESPACE
%{rlibdir}/eba/INDEX
%{rlibdir}/eba/Meta
%{rlibdir}/eba/help
%{rlibdir}/eba/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.0-1
- initial package for Fedora