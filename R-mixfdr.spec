%global packname  mixfdr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Computes false discovery rates and effect sizes using normal mixtures

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package fits normal mixture models to data and uses them to compute
effect size estimates and local and tail area false discovery rates. To
make this precise, suppose you have many normally distributed z's, and
each z[i] has mean delta[i]. This package will estimate delta[i] based on
the z's (effect sizes), P(delta[i]=0|z[i]) (local false discovery rates)
and P(delta[i]=0||z[i]|>z) (tail area false discovery rates).

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
%doc %{rlibdir}/mixfdr/html
%doc %{rlibdir}/mixfdr/DESCRIPTION
%{rlibdir}/mixfdr/Meta
%{rlibdir}/mixfdr/INDEX
%{rlibdir}/mixfdr/help
%{rlibdir}/mixfdr/NAMESPACE
%{rlibdir}/mixfdr/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora