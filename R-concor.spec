%global packname  concor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Concordance

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The four functions svdcp (cp for column partitioned), svdbip or svdbip2
(bip for bi-partitioned), and svdbips (s for a simultaneous optimization
of one set of r solutions), correspond to a "SVD by blocks" notion, by
supposing each block depending on relative subspaces, rather than on two
whole spaces as usual SVD does. The other functions, based on this notion,
are relative to two column partitioned data matrices x and y defining two
sets of subsets xi and yj of variables and amount to estimate a link
between xi and yj for the pair (xi, yj) relatively to the links associated
to all the other pairs.

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
%doc %{rlibdir}/concor/DESCRIPTION
%doc %{rlibdir}/concor/html
%{rlibdir}/concor/R
%{rlibdir}/concor/Meta
%{rlibdir}/concor/help
%{rlibdir}/concor/INDEX
%{rlibdir}/concor/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0.1-1
- initial package for Fedora