%global packname  QCA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Qualitative Comparative Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
Performs the Quine-McCluskey algorithm for Qualitative Comparative
Analysis, for both crisp versions: bvQCA (binary-value QCA) and for mvQCA
(multi-value QCA). In the classical approach it currently handles about 15
conditions and one outcome for binary data only, but since version 0.4-5
the package has an enhanced, faster function that obtains the same exact
solutions with a substantially lower memory consumption, it handles even
more causal conditions; the enhanced function eqmcc() can also be used for
mvQCA. The next versions of this algorithm will be oriented towards
fuzzy-set functions. Also, in the near future the current functions will
deal with missing values in the data

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
%doc %{rlibdir}/QCA/html
%doc %{rlibdir}/QCA/DESCRIPTION
%{rlibdir}/QCA/TODO
%{rlibdir}/QCA/Meta
%{rlibdir}/QCA/data
%{rlibdir}/QCA/CHANGES
%{rlibdir}/QCA/NAMESPACE
%{rlibdir}/QCA/INDEX
%{rlibdir}/QCA/R
%{rlibdir}/QCA/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- initial package for Fedora