%global packname  nlADG
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Regression in the Normal Linear ADG Model

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggm 

BuildRequires:    R-devel tex(latex) R-ggm 

%description
Regression in the Normal Linear ADG Model

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
%doc %{rlibdir}/nlADG/DESCRIPTION
%doc %{rlibdir}/nlADG/html
%{rlibdir}/nlADG/INDEX
%{rlibdir}/nlADG/help
%{rlibdir}/nlADG/R
%{rlibdir}/nlADG/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora