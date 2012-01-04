%global packname  cg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Comparison of groups

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc R-base R-utils R-methods R-stats R-graphics R-grid R-lattice R-MASS R-survival R-multcomp R-nlme 
Requires:         R-VGAM 

BuildRequires:    R-devel tex(latex) R-Hmisc R-base R-utils R-methods R-stats R-graphics R-grid R-lattice R-MASS R-survival R-multcomp R-nlme
BuildRequires:    R-VGAM 


%description
cg is comprehensive data analysis software, and stands for "compare
groups." Its genesis and evolution are driven by common needs to compare
administrations, conditions, etc. in medicine research & development. The
current version provides comparisons of unpaired samples, i.e. a linear
model with one factor of at least two levels. Good data graphs, modern
statistical methods, and useful displays of results are emphasized.

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
%doc %{rlibdir}/cg/html
%doc %{rlibdir}/cg/DESCRIPTION
%{rlibdir}/cg/NAMESPACE
%{rlibdir}/cg/Meta
%{rlibdir}/cg/data
%{rlibdir}/cg/R
%{rlibdir}/cg/INDEX
%{rlibdir}/cg/help
%{rlibdir}/cg/CHANGES

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora