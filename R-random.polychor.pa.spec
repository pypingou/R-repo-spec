%global packname  random.polychor.pa
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3.1
Release:          1%{?dist}
Summary:          A Parallel Analysis With Polychoric Correlation Matrices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-psych R-nFactors 

BuildRequires:    R-devel tex(latex) R-psych R-nFactors 

%description
The Function performs a parallel analysis using simulated polychoric
correlation matrices. The nth-percentile of the eigenvalues distribution
obtained from both the randomly generated and the real data polychoric
correlation matrices is returned. A plot comparing the two types of
eigenvalues (real and simulated) will help determine the number of real
eigenvalues that outperform random data. The function is based on the idea
that if real data are non-normal and the polychoric correlation matrix is
needed to perform a Factor Analysis, then the Parallel Analysis method
used to choose a non-random number of factors should also be based on
randomly generated polychoric correlation matrices and not on Pearson
correlation matrices. Version 1.1.1, fixed a minor bug in the regarding
the estimated time needed to complete the simulation. Also in this
version, the function is now able to manage supplied data.matrix in which
variables representing factors (i.e., variables with ordered categories)
are present and may cause an error when the Pearson correlation matrix is
calculated. Version 1.1.2 simply has updated the function that calculates
the polycoric correlation matrix due to changes in the psych() package.
Version 1.1.3 tackles two problems signalled by users: 1) the possibility
to make available the results of simulation for plotting them in other
softwares. Now the random.polychor.pa will show, upon request, all the
data used in the scree-plot.  2) The function polichoric() of the psych()
package does not handle data matrices that include 0 as possible category
and will cause the function to stop with error. So a check for the
detection of the 0 code within the provided data.matrix is now added and
will cause the random.polychor.pa function to stop with a warning message.

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
%doc %{rlibdir}/random.polychor.pa/DESCRIPTION
%doc %{rlibdir}/random.polychor.pa/html
%{rlibdir}/random.polychor.pa/R
%{rlibdir}/random.polychor.pa/Meta
%{rlibdir}/random.polychor.pa/help
%{rlibdir}/random.polychor.pa/INDEX
%{rlibdir}/random.polychor.pa/NAMESPACE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3.1-1
- initial package for Fedora