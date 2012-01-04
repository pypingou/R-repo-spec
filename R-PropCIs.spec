%global packname  PropCIs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Computes confidence intervals for single proportions, for differences in proportions, for an odds-ratio and for the relative risk in a 2x2 table

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Computes confidence intervals for single proportions and confidence
intervals for differences in proportions in a 2x2 table

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
%doc %{rlibdir}/PropCIs/NEWS
%doc %{rlibdir}/PropCIs/html
%doc %{rlibdir}/PropCIs/DESCRIPTION
%{rlibdir}/PropCIs/R
%{rlibdir}/PropCIs/NAMESPACE
%{rlibdir}/PropCIs/help
%{rlibdir}/PropCIs/INDEX
%{rlibdir}/PropCIs/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora