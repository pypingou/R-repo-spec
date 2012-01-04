%global packname  epoc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.4.13
Release:          1%{?dist}
Summary:          EPoC (Endogenous Perturbation analysis of Cancer)

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2.4-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lassoshooting R-Matrix R-methods R-irr R-igraph R-elasticnet R-survival 

BuildRequires:    R-devel tex(latex) R-lassoshooting R-Matrix R-methods R-irr R-igraph R-elasticnet R-survival 

%description
Estimates sparse matrices A or G using fast lasso regression from mRNA
transcript levels Y and CNA profiles U. Two models are provided, EPoC A
where AY + U + R = 0 and EPoC G where Y = GU + E, the matrices R and E are
so far treated as noise. For details see the reference and the manual page
of `lassoshooting'.

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
%doc %{rlibdir}/epoc/html
%doc %{rlibdir}/epoc/DESCRIPTION
%{rlibdir}/epoc/INDEX
%{rlibdir}/epoc/help
%{rlibdir}/epoc/LICENSE
%{rlibdir}/epoc/NAMESPACE
%{rlibdir}/epoc/R
%{rlibdir}/epoc/Meta
%{rlibdir}/epoc/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4.13-1
- initial package for Fedora