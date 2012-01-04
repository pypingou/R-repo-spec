%global packname  JointModeling
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Joint Modelling of Mean and Dispersion

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mgcv 

BuildRequires:    R-devel tex(latex) R-mgcv 

%description
Some functions useful to perform joint modelling of Mean and Dispersion
through two interlinked GLM's or GAM's.

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
%doc %{rlibdir}/JointModeling/DESCRIPTION
%doc %{rlibdir}/JointModeling/html
%{rlibdir}/JointModeling/R
%{rlibdir}/JointModeling/Meta
%{rlibdir}/JointModeling/help
%{rlibdir}/JointModeling/INDEX
%{rlibdir}/JointModeling/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora