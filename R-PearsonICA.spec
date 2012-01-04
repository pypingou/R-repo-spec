%global packname  PearsonICA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Independent component analysis using score functions from the Pearson system

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Pearson-ICA algorithm is a mutual information-based method for blind
separation of statistically independent source signals. It has been shown
that the minimization of mutual information leads to iterative use of
score functions, i.e. derivatives of log densities. The Pearson system
allows adaptive modeling of score functions. The flexibility of the
Pearson system makes it possible to model a wide range of source
distributions including asymmetric distributions. The algorithm is
designed especially for problems with asymmetric sources but it works for
symmetric sources as well.

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
%doc %{rlibdir}/PearsonICA/CITATION
%doc %{rlibdir}/PearsonICA/DESCRIPTION
%doc %{rlibdir}/PearsonICA/html
%{rlibdir}/PearsonICA/INDEX
%{rlibdir}/PearsonICA/NAMESPACE
%{rlibdir}/PearsonICA/help
%{rlibdir}/PearsonICA/R
%{rlibdir}/PearsonICA/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora