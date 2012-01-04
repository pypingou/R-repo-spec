%global packname  fpow
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Computing the noncentrality parameter of the noncentral F distribution

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Returns the noncentrality parameter of the noncentral F ditribution if
probability of type I and type II error, degrees of freedom of the
numerator and the denominator are given. It may be useful for computing
minimal detecable differences for general ANOVA models. This program is
documented in the paper of A. Baharev, S. Kemeny, On the computation of
the noncentral F and noncentral beta distribution; Statistics and
Computing, 2008, 18 (3), 333-340.
http://dx.doi.org/10.1007/s11222-008-9061-3 Preprint of this paper is
available at http://reliablecomputing.eu/ncbeta.html

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
%doc %{rlibdir}/fpow/DESCRIPTION
%doc %{rlibdir}/fpow/html
%{rlibdir}/fpow/R
%{rlibdir}/fpow/help
%{rlibdir}/fpow/INDEX
%{rlibdir}/fpow/Meta
%{rlibdir}/fpow/NAMESPACE
%{rlibdir}/fpow/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora